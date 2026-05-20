import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sqlSidebar: SidebarsConfig['SQL'] = [
  {
    type: 'category',
    label: 'SQL',
    items: [
      'sql/sql_basic_CRUD',
      'sql/sql_aggregate_fucntions',
      'sql/sql_joins',
      'sql/sql_advance_operator',
      

    ],
  },
];

export default sqlSidebar;