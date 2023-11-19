require 'spec_helper'

describe ComputerBase do
  attr_reader :computer

  before :each do
    @computer = ComputerBase.new
  end

  it "should return a random move when playing game theoretically optimal" do
    computer_decision = computer.play_gt_optimal

    expect([:p, :r, :s]).to include(computer_decision)
  end
end
