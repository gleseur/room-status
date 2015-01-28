if (Meteor.isServer) {
  Pwd = new Meteor.Collection("pwd");
  HTTP.methods({
    '/set_pwd/:pwd': function () {
      if (Pwd.findOne()) {
        this.setStatusCode(401);
      } else {
        Pwd.insert({value: this.params.pwd});
      }
    }
  });
}
