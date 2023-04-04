import unittest

from Assignment import create_filename,getHeaderArticles,get_main_articles,get_side_articles



class TestVerge(unittest.TestCase):

    def initSetup(self):
        test_url = "https://www.theverge.com/"

    def test_DMY(self):
        file_name = create_filename()
        self.assertTrue(file_name.endswith('_verge.csv'))

    def test_insert_header_articles(self):
        final = getHeaderArticles()
        self.assertEqual(len(final),1)
        self.assertEqual(final[0]['headline'],"Microsoft Flight Simulator tricked me into getting a pilot’s license")
        self.assertEqual(final[0]['url'],'https://www.theverge.com//23653862/msfs-home-flight-simulator-pilot')
        self.assertEqual(final[0]['author'],'Daniel Oberhaus')
        self.assertEqual(final[0]['date'],'Apr 3')

    def test_insert_main_articles(self):
        final = get_main_articles()
        self.assertEqual(final[0]['headline'],"Chemicals banned from air conditioners and refrigerators are making a comeback — and scientists don’t know why")
        self.assertEqual(final[0]['url'],'https://www.theverge.com//2023/4/3/23665293/cfcs-air-conditioning-refrigerants-ozone-depleting-chemicals-surprise-comeback')
        self.assertEqual(final[0]['author'],'Justine Calma')
        self.assertEqual(final[0]['date'],'Apr 3')

    def test_insert_side_articles(self):
        final = get_side_articles()
        self.assertEqual(final[0]['headline'],"Chemicals banned from air conditioners and refrigerators are making a comeback — and scientists don’t know why")
        self.assertEqual(final[0]['url'],'https://www.theverge.com//2023/4/3/23665293/cfcs-air-conditioning-refrigerants-ozone-depleting-chemicals-surprise-comeback')
        self.assertEqual(final[0]['author'],'Justine Calma')
        self.assertEqual(final[0]['date'],'Apr 3')


if __name__ == '__main__':
    unittest.main()