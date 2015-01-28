if (Meteor.isClient) {

  Template.main.rooms = function () {
      return Room.find().fetch();
  }

  Template.room.room_status = function () {
    return BusyTime.getLast(this.room_id).status;
  }

  Template.room.busy = function () {
    return BusyTime.getLast(this.room_id).status == BusyTime.BUSY;
  }
}
