const path = require("path");

module.exports = {
  entry: "./src/main.js",
  output: {
    filename: "./script.js",
    path: path.resolve(__dirname, ""),
  },
  resolve: {
    // changed from extensions: [".js", ".jsx"]
    extensions: [".ts", ".tsx", ".js", ".jsx"],
  },
  module: {
    rules: [
      // changed from { test: /\.jsx?$/, use: { loader: 'babel-loader' }, exclude: /node_modules/ },
      {
        test: /\.(t|j)sx?$/,
        use: { loader: "ts-loader" },
        exclude: /node_modules/,
      },

      // addition - add source-map support
      {
        enforce: "pre",
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "source-map-loader",
      },

      {
        test: /\.svg$/,
        use: ["@svgr/webpack"],
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  output: {
    filename: "script.js",
  },
  devtool: "source-map",
};
