const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const cons = require("consolidate");
const dust = require("dustjs-helpers");
const { Pool, Client } = require("pg");
const connectionString = "postgres://OSAMA:OSAMA@localhost/recipedb";
const client = new Client({
  connectionString: connectionString
});
// const client = new Client({
//   user: 'OSAMA',
//   host: 'localhost',
//   database: 'recipedb',
//   password: 'OSAMA',
//   port: 5432,
// })
client.connect(console.log('Connected to Postgres'));
const port = process.env.PORT || 3000;
const app = express();

app.engine("dust", cons.dust);
app.set("view engine", "dust");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  client.query("SELECT * FROM recipes", (err, result) => {
    if (err) {
      return console.error("error running query ", err);
    }
    // client.end(console.log('disconnected...'));
    res.render("index", {
      recipes: result.rows
    });
  });
});

app.listen(port, () => {
  console.log("Server started on port 3000");
});
