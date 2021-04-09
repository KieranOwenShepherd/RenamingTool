import unittest
import os
from glob import glob
import shutil
import renaming

class TestRenamingExample(unittest.TestCase):
    def setUp(self):
        # Create files, this assumes the directory has write access
        self.testfolder = os.path.join(os.path.split(__file__)[0],"testfolder")
        os.mkdir(self.testfolder)
        test_filenames = [
            "prodeng.11.jpg", "prodeng.11.png", "prodeng.27.jpg", "prodeng.32.jpg", 
            "prodeng.32.png", "prodeng.33.png", "prodeng.47.png", "prodeng.55.jpg", 
            "prodeng.55.png", "prodeng.56.jpg", "prodeng.68.jpg", "prodeng.72.png",
            "prodeng.94.png", 
            "weta.17.jpg", "weta.22.jpg", "weta.37.jpg", "weta.55.jpg", "weta.96.jpg"
        ]

        for fn in test_filenames:
            open(os.path.join(self.testfolder,fn), 'a').close()

    def tearDown(self):
        shutil.rmtree(self.testfolder)

    def _get_folder_contents(self):
        renamed = glob(os.path.join(self.testfolder,'*'))
        renamed = [path.strip(self.testfolder) for path in renamed]
        renamed.sort(key=lambda p: (p.split('.')[0],p.split('.')[-1],p.split('.')[-2]))
        return renamed


    def test_renamingexample(self):
        renaming.sequential_rename(self.testfolder)

        renamed = self._get_folder_contents()

        self.assertEqual(renamed, [
            "prodeng.01.jpg", "prodeng.02.jpg", "prodeng.03.jpg", "prodeng.04.jpg", 
            "prodeng.05.jpg", "prodeng.06.jpg", "prodeng.01.png", "prodeng.02.png", 
            "prodeng.03.png", "prodeng.04.png", "prodeng.05.png", "prodeng.06.png", 
            "prodeng.07.png", 
            "weta.01.jpg", "weta.02.jpg", "weta.03.jpg", "weta.04.jpg", "weta.05.jpg",
        ])

    def test_startingnumber(self):
        renaming.sequential_rename(self.testfolder, start=1001)

        renamed = self._get_folder_contents()

        self.assertEqual(renamed, [
            "prodeng.1001.jpg", "prodeng.1002.jpg", "prodeng.1003.jpg", "prodeng.1004.jpg", 
            "prodeng.1005.jpg", "prodeng.1006.jpg", "prodeng.1001.png", "prodeng.1002.png", 
            "prodeng.1003.png", "prodeng.1004.png", "prodeng.1005.png", "prodeng.1006.png", 
            "prodeng.1007.png", 
            "weta.1001.jpg", "weta.1002.jpg", "weta.1003.jpg", "weta.1004.jpg", "weta.1005.jpg",
        ])

    
    def test_extrapadding(self):
        renaming.sequential_rename(self.testfolder, pad=4)

        renamed = self._get_folder_contents()

        self.assertEqual(renamed, [
            "prodeng.0001.jpg", "prodeng.0002.jpg", "prodeng.0003.jpg", "prodeng.0004.jpg", 
            "prodeng.0005.jpg", "prodeng.0006.jpg", "prodeng.0001.png", "prodeng.0002.png", 
            "prodeng.0003.png", "prodeng.0004.png", "prodeng.0005.png", "prodeng.0006.png", 
            "prodeng.0007.png", 
            "weta.0001.jpg", "weta.0002.jpg", "weta.0003.jpg", "weta.0004.jpg", "weta.0005.jpg",
        ])



if __name__ == '__main__':
    unittest.main()