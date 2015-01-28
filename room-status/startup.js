if (Meteor.isServer) {
    Meteor.startup(function () {
        if (Room.find().count() == 0) {
            Room.insert({
                room_id: 1,
                name: "man"
            });
            Room.insert({
                room_id: 2,
                name: "woman"
            });
        }
        if (BusyTime.find().count() == 0) {
            BusyTime.insert({
                room_id: 1,
                opened_at: moment().toDate(),
                status: "free"
            });
            BusyTime.insert({
                room_id: 2,
                opened_at: moment().toDate(),
                status: "free"
            });
        }
    });
}
