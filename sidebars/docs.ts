import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const docsSidebar: SidebarsConfig['docs'] = [
  'commons/intro',
  'commons/git_intro',
  'commons/docusaurus-all-features',
  'commons/html_notes',
  'commons/uv_intro',
  {
    type: 'category',
    label: 'SQLalchemy',
    items: [
      'commons/sqlalchemy/sqlalchemy_quick_start',
      'commons/sqlalchemy/sqlalchemy_models',
      'commons/sqlalchemy/sqlalchemy_engine',
      'commons/sqlalchemy/sqlalchemy_basic_crud',
    ],
  },
  {
    type: 'category',
    label: 'Alembic',
    items: [
      'commons/alembic/alembic_async',
      'commons/alembic/alembic_sync',
    ],
  },
  {
    type: 'category',
    label: 'Mermaid',
    items: [
      'commons/mermaid/mermaid_class_diagram',
    ],
  },
  {
    type: 'category',
    label: 'UML-Diagram',
    items: [
      'commons/uml_class/uml_class_diagram',
      'commons/uml_class/uml_full_interview_qna',
      'commons/uml_class/uml_full_detailed_interview',
    ],
  },
  {
    type: 'category',
    label: 'SOLID Principle',
    items: [
      'commons/solid_principle/solid_principle_basic',
    ],
  },
];

export default docsSidebar;