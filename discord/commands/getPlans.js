//jshint esversion:9

module.exports = {
    name: "plan",
	description: 'get plan',
    execute(message, args) {
        async function getUser() {
  try {
    const response = await axios.get('/user?ID=12345');
      message.channel.send(response);
  } catch (error) {
    message.channel.send("Sorry bot down")
  }
}
	},
};