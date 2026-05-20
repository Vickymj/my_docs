import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const djangoSidebar: SidebarsConfig['Django'] = [
  {
    type: 'category',
    label: 'Django Basic',
    items: [
      'django/django_installtion_setup',
      'django/django_basic_CRUD',
      
    ],
  },
  {
    type: 'category',
    label: 'DRF',
    items: [
      'django/drf/drf_quickstart',
      'django/drf/drf_basic_CRUD',
      'django/drf/drf_serializer',
      'django/drf/drf_viewset',
      'django/drf/drf_class_based_view',
      'django/drf/drf_swagger',
    ],
  }
];
export default djangoSidebar;