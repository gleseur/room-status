if (Meteor.isClient) {
  Template.registerHelper("equals", function (a, b) {
      return (a == b);
  });

  Session.setDefault('view', 'main');

  Template.main.helpers({
      view: function () {return Session.get('view')},
      rooms: function () {return Room.find().fetch()},
      stats: function () {return Stats.find().fetch();}
  });

  Template.room.helpers({
      room_status: function () { return BusyTime.getLast(this.room_id).status;},
      busy: function () { return BusyTime.getLast(this.room_id).status == "busy";}
  });

}
