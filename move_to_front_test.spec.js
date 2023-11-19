/* I think you can run this file from command line with jasmine-node move_to_front_test.spec.js */

var moveToFront = require('./move_to_front');

describe('moveToFront', function() {
  it('test 1', function() {
    var back = [4,5,6]
    var front = [1,2,3]
    var combined = moveToFront(back, front);

    expect(combined).toEqual([1,2,3,4,5,6]);
  });

  it('test 2', function() {
    var back = [4,5,6]
    var front = [1,2,3,4]
    var combined = moveToFront(back, front);

    expect(combined).toEqual([1,2,3,4,5,6]);
  });

  it('test 3', function() {
    var entire = [1,2,3,4,5,6]
    var front = [1,2,3,4]
    var combined = moveToFront(entire, front);

    expect(combined).toEqual([1,2,3,4,5,6]);
  });

});
