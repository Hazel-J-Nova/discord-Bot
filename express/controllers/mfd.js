//jshint esversion:9

const Mfd = require("../models/mfd")


module.exports.index = async (req, res) => {
    const plans = await Mfd.find({});
    res.json(plans);
};

module.exports.new = async (req, res) => {
    const newPlan = new Mfd({
        name: req.body.name,
        votes: req.body.votes,
        plan: req.body.plan,
        url: req.body.url,
        author: req.body.author
    });
    await newPlan.save();
    res.json(newPlan);
};

module.exports.edit = async (req, res) => {
   const plan =  await Mfd.findOneAndUpdate({ name: req.body.name },{votes:req.body.votes, plan:req.body.plan }, [options.new=false])
    res.json(plan)
}


module.exports.show = async (req, res) => {
    const plan = await Mfd.findOne({ name: req.params.name });
    res.json(plan)
}

module.exports.delete = async (req, res) => {
    await Mfd.deleteMany({});
};