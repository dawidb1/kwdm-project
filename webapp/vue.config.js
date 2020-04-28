module.exports = {
  devServer: {
    proxy: {
      '^/orthanc': {
        target: 'http://nginx:80',
        changeOrigin: true
      },
      '^/predict': {
        target: 'http://segmentation:5000',
        changeOrigin: true
      },
    },
  },
};
