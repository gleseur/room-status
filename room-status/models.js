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
                $gte: moment().subtract('month', 1).toDate()
            }
        });
    }
}

if (Meteor.isClient) {
    Meteor.subscribe("busy_times");
}


Room = new Meteor.Collection('room');
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
