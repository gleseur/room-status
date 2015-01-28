if (Meteor.isServer) {
  Pwd = new Meteor.Collection("pwd");
  HTTP.methods({
      '/set_pwd/:pwd': function () {
          if (Pwd.findOne()) {
              this.setStatusCode(401);
          } else {
              Pwd.insert({value: this.params.pwd});
          }
      },

      'set_status/:room_id/:status': function () {
          pwd = Pwd.findOne()
          if (pwd && this.query.pwd && pwd.value === this.query.pwd) {
              room_id = parseInt(this.params.room_id);
              busy_time = BusyTime.getLast(room_id);
              if (busy_time.status != this.params.status) {
                  // This is a new period
                  // Closing current time
                  BusyTime.update(busy_time.id, {
                      $set: {closed_at: moment().toDate()}
                  });
                  // Creating a new one
                  BusyTime.insert({
                      status: this.params.status,
                      room_id: room_id,
                      opened_at: moment().toDate()
                  });
              }
          } else {
              this.setStatusCode(401);
          }
      }
  });
}
