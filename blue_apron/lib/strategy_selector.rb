Dir["./lib/computer_strategies/*.rb"].each {|file| require file }

class StrategySelector
  attr_reader :strategy

  def initialize(strategy)
    @strategy = strategy.downcase
  end

  def determine_computer
    case strategy
    when "favorite"
      ComputerFavorite.new
    when "last"
      ComputerLast.new
    when "champ"
      ComputerChamp.new
    end
  end
end
