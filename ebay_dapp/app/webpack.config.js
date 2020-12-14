const path = require("path");
const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  mode: 'development',
  entry: "./src/index.js",
  output: {
    filename: "index.js",
    path: path.resolve(__dirname, "dist"),
  },
  // module: {
  //   rules:[
  //       {
  //           test:/\.js$/,
  //           loader:'babel-loader',
  //           include:path.join(__dirname,'src'),
  //           exclude: /node_modules/
  //       }
  //   ]
  // },
  plugins: [
    new CopyWebpackPlugin([{ from: "./src/index.html", to: "index.html" }]),
    new CopyWebpackPlugin([{ from: "./src/list-item.html", to: "list-item.html" }]),
    new CopyWebpackPlugin([{ from: "./src/product.html", to: "product.html" }]),
  ],
  devServer: { contentBase: path.join(__dirname, "dist"), compress: true },
};
