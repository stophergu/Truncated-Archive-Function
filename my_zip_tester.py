import unittest, shutil, os, tempfile, my_zip_file, zipfile
orig = os.getcwd()
path = os.path.abspath('tester')


class Test_archiver(unittest.TestCase):

    def setUp(self):
        #set up a tempfile for testing to be deleted on tearDown
        self.orig = os.getcwd()
        self.path = tempfile.mkdtemp()
        self.zip_fn = os.path.basename(self.path) + '.zip'
        #Populate Temp Path with files and directories for testing
        os.chdir(self.path)
        self.files = ['test_file', 'test_file.ext'] 
        for fn in self.files:
            open(fn, 'w').close()
        self.dirs = ['test_folder', 'bogus_test_folder.ext']
        for dir_name in self.dirs:
            os.mkdir(dir_name)
        os.chdir(self.orig)

        
    def test_func_archiver(self):
        my_zip_file.archiver(self.path) 
        #Observed/Expected
        zf = zipfile.ZipFile(self.zip_fn)
        observed = zf.namelist()
        expected = [os.path.join(os.path.basename(self.path),fn)
                               .replace('\\', '/') for fn in self.files]

        #tests       
        self.assertEqual(sorted(observed), sorted(expected),
                        '\nObserved does not equal Expected:\
                        \nExpected: {0}\
                        \nObserved: {1}'.
                        format(expected, observed))

        for folder in self.dirs:
            self.assertTrue(os.path.join(self.path, folder) not in observed,
                            'The subdirectory {0} was archived'.
                            format(folder))
        for fn in self.files:
            archived_file = os.path.join(os.path.basename(self.path), fn)
            self.assertTrue(archived_file.replace('\\', '/') in observed,
                            '{0} was not archived'.format(fn))     

    def tearDown(self):
        shutil.rmtree(self.path)
        

if __name__ == "__main__":
    unittest.main()
