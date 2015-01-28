BusyTime = new Meteor.Collection('busy_time');
/*
 * This collection represents the moments when the detector detected some
 * presence you know where
 * Following fields are present:
 *  - room_id: mongoid of the corresponding room object
 *  - opened_at: datetime indicating when it started
 *  - closed_at: end_time on when it ended
 */

// Nothing is allowed

// Limiting publishing of last month data
if (Meteor.isServer) {
    Meteor.publish("busy_times", function () {
        return BusyTime.find({
            opened_at: {
                $gte: moment().subtract(1, 'month').toDate()
            }
        });
    });
}

if (Meteor.isClient) {
    Meteor.subscribe("busy_times");
}

BusyTime.BUSY == "busy";
BusyTime.FREE == "free";
BusyTime.getLast = function (room_id) {
    return BusyTime.find(
        {room_id: room_id},
        {
            sort: {opened_at: -1},
            limit: 1
        }
    ).fetch()[0];
}

Room = new Meteor.Collection('room');
// room_id
// name
// Nothing allowed
// publish all
if (Meteor.isServer) {
    Meteor.publish("rooms", function () {
        return Room.find();
    });
}

if (Meteor.isClient) {
    Meteor.subscribe("rooms");
}
