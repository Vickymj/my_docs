import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sqlSidebar: SidebarsConfig['Flask'] = [
  {
    type: 'category',
    label: 'Flask Docs',
    items: [
        'flask/flask_basic_CRUD',
        'flask/flask_auto_reload',  
        'flask/flask_smorest',  
        'flask/flask_marshmallow',
    ],
  },
];

export default sqlSidebar;