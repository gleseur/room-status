if (Meteor.isServer) {
    Meteor.startup(function () {
        Room.remove({});
        BusyTime.remove({});
        Room.insert({
            room_id: 1,
            name: "man"
        });
        Room.insert({
            room_id: 2,
            name: "woman"
        });
        BusyTime.insert({
            room_id: 1,
            opened_at: moment().toDate(),
            status: "free"
        });
        BusyTime.insert({
            room_id: 2,
            opened_at: moment().toDate(),
            status: "busy"
        });
    });
}
