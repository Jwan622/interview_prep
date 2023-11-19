require 'stringio'

require './lib/rps_game'
require './lib/input_evaluator'
require './lib/messages'
require './lib/scorer'
require './lib/score_keeper'
require './lib/moves_tracker'
require './lib/strategy_selector'
require './lib/argv_checker'

Dir["./lib/computer_strategies/*.rb"].each {|file| require file }
