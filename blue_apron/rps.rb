require './lib/rps_game'
require './lib/argv_checker'

class RpsRunner
  def start(strategy, input_stream, output_stream)
    RpsGame.new(strategy, input_stream, output_stream).play
  end
end

cleaned_argv = ARGVChecker.process(ARGV)
strategy, input_stream, output_stream = cleaned_argv[0], cleaned_argv[1], cleaned_argv[2]
puts Messages.invalid_strategy if strategy != ARGV[0]
puts Messages.invalid_input_stream if input_stream != ARGV[1] && ARGV[1] != nil
puts Messages.invalid_output_stream if output_stream != ARGV[2] && ARGV[1] != nil
RpsRunner.new.start(strategy, input_stream, output_stream)
