from django.test import TestCase

from coopInfo.models import Person , Cooperative, content_file_name

class PersonContentFileNameTest(TestCase):

    def testSubmitAJpegWithName(self):

        aPerson  = Person()
        currentFileName = "bob-19282.jpg"
        aPerson.name = "Bob Biture"

        aCoop = Cooperative()
        aCoop.id = 12

        aPerson.coopId = aCoop 

        result = content_file_name(aPerson, currentFileName)
        self.assertEqual(result, "persons/BobBiture-12.jpg")

    def testSubmitAJpegWithNameWithSpecialChar(self):

        aPerson  = Person()
        currentFileName = "bob-19282.jpg"
        aPerson.name = "Bob H. \"bubba\" Machin"

        aCoop = Cooperative()
        aCoop.id = 12

        aPerson.coopId = aCoop 

        result = content_file_name(aPerson, currentFileName)
        self.assertEqual(result, "persons/BobHbubbaMachin-12.jpg")