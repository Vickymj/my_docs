import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const fastapiSidebar: SidebarsConfig['FastAPI'] = [
  {
    type: 'category',
    label: 'Basic - CRUD',
    items: [
      'fastapi/fastapi_intro',
      'fastapi/fastapi_body',
      'fastapi/fastapi_response_model',
      'fastapi/fastapi_sql_relation_db',
      'fastapi/fastapi_structured',
      'fastapi/fastapi_authentication',
      'fastapi/fatapi_pydantic_CRUD',

      // 'fastapi/type_hinting_annotation',
      // 'fastapi/decorator',
      // 'fastapi/fastapi_basic_CRUD',
      // 'fastapi/python_pydantic',
      // 'fastapi/fastapi_db_session',
      // 'fastapi/python_async',
    ],
  },
];

export default fastapiSidebar;