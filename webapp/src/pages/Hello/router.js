const Hello = () => import('./index');

const helloRoutes = {
  name: 'hello',
  path: '/hello',
  component: Hello,
};

export default helloRoutes;
