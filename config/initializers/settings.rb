if Rails.env.production?
  # update whenever crontab's jobs
  `whenever --update-crontab`
else
  Hirb.enable

  old_print = Pry.config.print
  Pry.config.print = proc do |*args|
    Hirb::View.view_or_page_output(args[1]) || old_print.call(*args)
  end
end
