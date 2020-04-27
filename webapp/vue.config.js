module.exports = {
  devServer: {
    proxy: {
      '^/orthanc': {
        target: 'http://nginx:80',
        changeOrigin: true
      },
    },
  },
};
