const mongooseConfig = { 
  useNewUrlParser: true,
  useFindAndModify: false,
  useCreateIndex: true, 
};
console.log("mongooseConfig", mongooseConfig)
module.exports = mongooseConfig;
