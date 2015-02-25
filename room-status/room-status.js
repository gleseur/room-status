if (Meteor.isClient) {
  Session.setDefault('view_stats', false);

  Template.main.helpers({
      view_stats: function () {return Session.get('view_stats')},
      rooms: function () {return Room.find().fetch()}
  });

  Template.stats.helpers({
      stats: function () {return Stats.find({}, {sort: {order: 1}}).fetch();},
      hourlies: function () {
        var max = HourlyStats.find({}, {sort: {value: -1}, limit: 1}).fetch()[0].value;
        return HourlyStats.find({}, {sort: {hour: 1}});
      }
  });

  Template.main.events = {
    'click .btn': function () {Session.set('view_stats', !Session.get('view_stats'))}
  }

  Template.room.helpers({
      room_status: function () { return BusyTime.getLast(this.room_id).status;},
      busy: function () { return BusyTime.getLast(this.room_id).status == "busy";}
  });


}
