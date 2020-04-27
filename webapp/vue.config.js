module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: 'https://dog.ceo/',
        changeOrigin: true
      },
    },
  },
};
