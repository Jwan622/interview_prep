require_relative 'computer_base'

class ComputerFavorite < ComputerBase
  attr_reader :strategy_name

  def initialize
    @strategy_name = "favorite"
  end

  def make_decision(tally)
    if tally.values.reduce(:+) <= 1
      play_gt_optimal
    else
      highest_tally_number = tally.values.max
      user_fav_move = tally.select { |decision, count| count == highest_tally_number }.keys.sample
      BEATS.key(user_fav_move)
    end
  end
end
