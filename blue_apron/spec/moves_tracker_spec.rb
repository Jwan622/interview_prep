require 'spec_helper'

describe MovesTracker do
  attr_reader :moves_tracker

  before :each do
    @moves_tracker = MovesTracker.new
  end

  it "correctly initializes with a blank tally with no moves for rock, paper, or scissor" do
    expect(moves_tracker.tally). to eql({ r: 0, p: 0, s: 0 })
  end

  it "correctly increments the right move" do
    moves_tracker.update(:r)
    expect(moves_tracker.tally). to eql({ r: 1, p: 0, s: 0 })

    moves_tracker.update(:r)
    expect(moves_tracker.tally). to eql({ r: 2, p: 0, s: 0 })

    moves_tracker.update(:p)
    moves_tracker.update(:p)

    expect(moves_tracker.tally). to eql({ r: 2, p: 2, s: 0 })

    moves_tracker.update(:s)
    moves_tracker.update(:p)
    expect(moves_tracker.tally). to eql({ r: 2, p: 3, s: 1 })
  end
end
