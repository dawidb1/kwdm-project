module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: 'https://localhost:8042/',
        ws: true,
        changeOrigin: true,
      },
    },
  },
};
