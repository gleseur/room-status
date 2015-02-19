BusyTime = new Meteor.Collection('busy_time');
/*
 * This collection represents the moments when the detector detected some
 * presence you know where
 * Following fields are present:
 *  - room_id: mongoid of the corresponding room object
 *  - opened_at: datetime indicating when it started
 *  - closed_at: end_time on when it ended
 *  - status: "free" or "busy"
 */

// Nothing is allowed

// Limiting publishing of last month data
if (Meteor.isServer) {
    Meteor.publish("busy_times", function () {
        return BusyTime.find({
            opened_at: {
                $gte: moment().subtract(3, 'days').toDate()
            }
        });
    });
}

if (Meteor.isClient) {
    Meteor.subscribe("busy_times");
}

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

Stats = new Meteor.Collection('usage_stats');
// name
// text
// value

// Nothing allowed
// publish all
if (Meteor.isServer) {
    Meteor.publish("stats", function () {
        return Stats.find();
    });
}

if (Meteor.isClient) {
    Meteor.subscribe("stats");
}

HourlyStats = new Meteor.Collection('hourly_stats');
// hour
// value

// Nothing allowed
// publish all
if (Meteor.isServer) {
    Meteor.publish("hourly_stats", function () {
        return HourlyStats.find();
    });
}

if (Meteor.isClient) {
    Meteor.subscribe("hourly_stats");
}

RoomHourlyStats = new Meteor.Collection('room_hourly_stats');
// hour
// value

// Nothing allowed
// publish all
if (Meteor.isServer) {
    Meteor.publish("room_hourly_stats", function () {
        return RoomHourlyStats.find();
    });
}

if (Meteor.isClient) {
    Meteor.subscribe("room_hourly_stats");
}
