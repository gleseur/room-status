if (Meteor.isClient) {

  Template.main.rooms = function () {
      return Room.find().fetch();
  }

  Template.room.busy = function () {
    return BusyTime.getLast(this.room_id).status == BusyTime.BUSY;
  }
}
