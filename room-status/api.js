if (Meteor.isServer) {
    Pwd = new Meteor.Collection("pwd");
    HTTP.methods({
      'set_status/:room_id/:status': function () {
          var pwd = Pwd.findOne()
          if (pwd && this.query.pwd && pwd.value === this.query.pwd) {
              var room_id = parseInt(this.params.room_id);
              var busy_time = BusyTime.getLast(room_id);
              if (busy_time.status != this.params.status) {
                  // This is a new period
                  // Closing current time
                  BusyTime.update(busy_time.id, {
                      $set: {closed_at: moment().toDate()}
                  });
                  // Creating a new one
                  var now = moment()
                  BusyTime.insert({
                      status: this.params.status,
                      room_id: room_id,
                      opened_at: now.toDate()
                  });
                  if (this.params.status == "busy") {
                      incStats(room_id, moment(busy_time.opened_at), now);
                  }
                  if (this.params.status == "free") {
                      checkLongest(busy_time.opened_at, now);
                  }
              }
          } else {
              this.setStatusCode(401);
          }
      }
    });

    function incStats(room_id, end_of_previous, start_of_current) {
        var name = (room_id == 1) ? "man_count_day" : "woman_count_day";
        var same_day = end_of_previous.day() == start_of_current.day();
        var setter = same_day ? {$inc: {value: 1}} : {$set: {value: 1}};
        Stats.update({name: name}, setter);
        Stats.update({name: "day_count"}, setter);
        Stats.update({name: "total_count"}, {$inc: {value: 1}});
    }

    function checkLongest(start, end) {
        var selector = {name: "longest_session"};
        var current_longest = Stats.findOne(selector).value;
        var contestant = Math.ceil((end-start)/1000);
        if (current_longest < contestant) {
            Stats.update(selector,  {$set: {value: contestant}});
        }
    }
}
