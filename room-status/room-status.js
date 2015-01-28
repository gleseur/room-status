if (Meteor.isClient) {

  Template.main.helpers({
      rooms: function () {return Room.find().fetch()}
  });

  Template.room.helpers({
      room_status: function () { return BusyTime.getLast(this.room_id).status;},
      busy: function () { return BusyTime.getLast(this.room_id).status == "busy";}
  });
}
