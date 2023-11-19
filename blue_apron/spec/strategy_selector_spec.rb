require 'spec_helper'

describe StrategySelector do
  attr_reader :computer

  it "initializes with a strategy" do
    @computer = StrategySelector.new("some strategy")

    expect(computer.strategy).to eql("some strategy")
  end

  it "can return an instance of the ComputerFavorite class" do
    strat_selector_fav = StrategySelector.new("favorite")

    expect(strat_selector_fav.determine_computer).to be_an(ComputerFavorite)
  end

  it "can return an instance of the ComputerLast class" do
    strat_selector_last = StrategySelector.new("last")

    expect(strat_selector_last.determine_computer).to be_an(ComputerLast)
  end

  it "can return an instance of the ComputerChamp class" do
    strat_selector_last = StrategySelector.new("last")

    expect(strat_selector_last.determine_computer).to be_an(ComputerLast)
  end
end
