if (Meteor.isClient) {

  Template.main.helpers({
      rooms: function () {return Room.find().fetch()},
      stats: function () {return [
        {name: "How Much Men's Today?", className: "man_count_day", value: 10},
        {name: "How Much Women's Today?", className: "woman_count_day", value: 15},
        {name: "Today's Usage", className: "day_count", value: 25},
        {name: "Total Number of Bathroom Use", className: "total_count", value: 55},
        {name: "Longest Session", className: "longest_session", value: 34},
        {name: "Busiest Day of the Week", className: "busiest_day", value: 'Monday'}
        ]}
  });

  Template.room.helpers({
      room_status: function () { return BusyTime.getLast(this.room_id).status;},
      busy: function () { return BusyTime.getLast(this.room_id).status == "busy";}
  });

}