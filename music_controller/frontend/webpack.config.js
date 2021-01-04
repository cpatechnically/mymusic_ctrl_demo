const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js", //entry point for the JS file
  output: {
    path: path.resolve(__dirname, "./static/frontend"), //relative path - static folder.
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true, //minimize to save space/increase speed
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
