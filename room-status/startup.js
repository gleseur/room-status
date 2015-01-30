if (Meteor.isServer) {
    Meteor.startup(function () {
        if (Room.find().count() == 0) {
            Room.insert({
                room_id: 1,
                text: "man"
            });
            Room.insert({
                room_id: 2,
                text: "woman"
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
        if (Stats.find().count() == 0) {
            Stats.insert({
                text: "How Many Men's Today?",
                name: "man_count_day",
                value: 0,
                order: 0
            });
            Stats.insert({
                text: "How Many Women's Today?",
                name: "woman_count_day",
                value: 0,
                order: 1
            });
            Stats.insert({
                text: "Today's Usage",
                name: "day_count",
                value: 0,
                order: 2
            });
            Stats.insert({
                text: "Total Usage",
                name: "total_count",
                value: 0,
                order: 3
            });
            Stats.insert({
                text: "Longest Session",
                name: "longest_session",
                value: 0,
                order: 4
            });
        }
    });
}
