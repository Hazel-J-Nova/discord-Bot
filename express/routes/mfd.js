//jshint esversion:9

const express = require("express");
const router = express.Router();
const catchAsync = require("../utils/catchAsync");


router.get("/", catchAsync(mfd.index));

router.post("/", catchAsync(mfd.new));

router.get("/:mfdPlan", catchAsync(mfd.show));

router.put("/:mfdPlan", catchAsync(mfd.edit));

router.delete("/", catchAsync(mfd.delete));


module.exports = router;