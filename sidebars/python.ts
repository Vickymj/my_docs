import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const pythonSidebar: SidebarsConfig['Python'] = [
  {
    type: 'category',
    label: 'Python',
    items: [
      'python/python_sheetcode',
      'python/python_intro',
      'python/python_variables',
      'python/python_private_variables',
      'python/python_data_types',
      'python/python_type_casting',
      'python/python_operators',
      'python/python_comments',
      'python/python_walrus_operator',
      'python/python_control_flow',
      'python/python_loops',
      'python/python_functions',
      'python/python_string',
      'python/python_lists',
      'python/python_tuples',
      'python/python_named_tuples',
      'python/python_sets',
      'python/python_dictionaries',
      'python/python_oop',
      
      
      
    ],
  },
  {
    type: 'category',
    label: 'Python List',
    items: [
      'python/python_list/python_list_basic',
      'python/python_list/python_list_quiz',
      'python/python_list/python_list_exercises',
    ],
  },
  {
    type: 'category',
    label: 'Python Dict',
    items: [
      'python/python_dict/python_dict_basic',
      'python/python_dict/python_dict_quiz',
      'python/python_dict/python_dict_exercises',
    ],
  },
  {
    type: 'category',
    label: 'Python Tuple',
    items: [
      'python/python_tuple/python_tuple_basic',
      'python/python_tuple/python_tuple_quiz',
      'python/python_tuple/python_tuple_exercises',
    ],
  },
  {
    type: 'category',
    label: 'Python LinkedList',
    items: [
      'python/big_O/linked_list/python_linked_list_basic',
      'python/big_O/linked_list/python_linked_list_quiz',
      'python/big_O/linked_list/python_linked_list_exercises',
    ],
  },
  {
    type: 'category',
    label: 'Python Functions & Modules',
    items: [
      'python/python_intro',
      'python/python_variables',
    ],
  },
  'python/python_interview_questions',
];

export default pythonSidebar;