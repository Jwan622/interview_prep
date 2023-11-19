require_relative 'strategy_selector'
require_relative 'scorer'
require_relative 'messages'
require_relative 'input_evaluator'
require_relative 'moves_tracker'
require_relative 'score_keeper'
require_relative 'printer'

class RpsGame
  attr_reader :input_stream,
              :output_stream,
              :scorer,
              :strategy_selector,
              :computer,
              :printer,
              :score_keeper,
              :input_evaluator,
              :moves_tracker,
              :user_input,
              :comp_decision

  def initialize(strategy, input_stream = $stdin, output_stream = $stdout)
    @input_stream = input_stream
    @output_stream = output_stream
    @scorer = Scorer.new
    @strategy_selector = StrategySelector.new(strategy)
    @computer = strategy_selector.determine_computer
    @printer = Printer.new(output_stream)
    @score_keeper = ScoreKeeper.new
    @input_evaluator = InputEvaluator.new
    @moves_tracker = MovesTracker.new
  end

  def play
    printer.print(Messages.introduction(computer.strategy_name))

    while user_input != :q
      printer.print(Messages.display_options)
      @user_input = input_stream.gets.chomp.to_sym
      obtain_valid_user_input
      user_chooses_q ? break : play_rps_and_keep_score
    end
    printer.print(Messages.end_game)
  end

  private

  def play_rps_and_keep_score
    track_user_move_and_computer_responds
    declare_winner_and_update_score
  end

  def track_user_move_and_computer_responds
    moves_tracker.update(user_input)
    @comp_decision = computer.make_decision(moves_tracker.tally)
  end

  def declare_winner_and_update_score
    victor_and_declaration = scorer.evaluate_round(comp_decision, user_input)
    printer.print(Messages.computer_play_and_eval(comp_decision.to_s, victor_and_declaration[:declaration]))
    current_standings = score_keeper.increments(victor_and_declaration)
    printer.print(Messages.announce_score(current_standings[:user], current_standings[:computer], current_standings[:tie]))
  end

  def obtain_valid_user_input
    while input_evaluator.is_invalid?(user_input)
      printer.print(Messages.invalid_input)
      printer.print(Messages.display_options)
      @user_input = input_stream.gets.chomp.to_sym
    end
  end

  def game_just_started
    moves_tracker.tally.values.reduce(:+) <= 1
  end

  def user_chooses_q
    user_input == :q
  end
end
