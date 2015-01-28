if (Meteor.isServer) {
    Meteor.startup(function () {
        Room.remove({});
        BusyTime.remove({});
        Room.insert({
            room_id: 1,
            name: "Boys"
        });
        Room.insert({
            room_id: 2,
            name: "Girls"
        });
        BusyTime.insert({
            room_id: 1,
            opened_at: moment().toDate(),
            status: BusyTime.BUSY
        });
        BusyTime.insert({
            room_id: 2,
            opened_at: moment().toDate(),
            status: BusyTime.FREE
        });
    });
}
