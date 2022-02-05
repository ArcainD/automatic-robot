import unittest
from unittest.mock import patch
import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.docs = app.documents
        self.dirs = app.directories
        self.number = ['10006', '11-2']
        self.docs_info = ['passport "2207 876234" "Василий Гупкин"',
                          'invoice "11-2" "Геннадий Покемонов"',
                          'insurance "10006" "Аристарх Павлов"']
        self.doc_info = 'passport "2207 876234" "Василий Гупкин"'

    def tearDown(self):
        app.documents = [
            {"type": "passport", "number": "2207 876234",
             "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2",
             "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006",
             "name": "Аристарх Павлов"}
        ]

        app.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    def test_show_document_info(self):
        self.assertEqual(app.show_document_info(self.docs[0]), self.doc_info)

    def test_show_all_docs_info(self):
        self.assertEqual(app.show_all_docs_info(), self.docs_info)

    def test_check_document_existence(self):
        for i in self.docs:
            self.assertTrue(app.check_document_existance(i['number']))

    def test_get_doc_owner_name(self):
        for i in self.docs:
            with patch('builtins.input', return_value=i['number']):
                self.assertEqual(app.get_doc_owner_name(), i['name'])

    def test_get_all_doc_owners_names(self):
        self.assertSetEqual(
            set([i['name'] for i in self.docs]),
            app.get_all_doc_owners_names()
        )

    def test_remove_doc_from_shelf(self):
        self.assertIn(self.number[0], self.dirs.get('2'))
        app.remove_doc_from_shelf(self.number[0])
        self.assertNotIn(self.number[0], self.dirs.get('2'))

    @unittest.expectedFailure
    def test_remove_doc_from_shelf_2(self):
        app.remove_doc_from_shelf(self.number[1])
        self.assertIn(
            app.remove_doc_from_shelf(self.number[1]),
            self.dirs.get('1')
        )

    def test_add_new_shelf(self):
        with patch('builtins.input', return_value='5'):
            self.assertTrue(app.add_new_shelf())

    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf(self.number[1], '3')
        self.assertIn(self.number[1], self.dirs.get('3'))

    def test_delete_doc(self):
        with patch('builtins.input', return_value=self.number[1]):
            app.delete_doc()
            self.assertNotIn(self.number[1], [i['number'] for i in self.docs])

    def test_get_doc_shelf(self):
        with patch('builtins.input', return_value=self.number[0]):
            self.assertEqual(app.get_doc_shelf(), '2')

    def test_move_doc_to_shelf(self):
        with patch('builtins.input', side_effect=['10006', '3']):
            app.move_doc_to_shelf()
            self.assertIn('10006', self.dirs['3'])

    def test_add_new_doc(self):
        with patch('builtins.input',
                   side_effect=['322', 'passport', 'Donald Duck', '3']
                   ):
            app.add_new_doc()
            self.assertIn(
                {"type": "passport", "number": "322", "name": "Donald Duck"},
                self.docs)
            self.assertIn("322", self.dirs['3'])
