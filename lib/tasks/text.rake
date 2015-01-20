# encoding: utf-8

namespace :text do
  desc 'verileri yükle'
  task :load => :environment do
    [
      'dunya',
      'ekonomi',
      'genel',
      'guncel',
      'kultur-sanat',
      'magazin',
      'planet',
      'saglik',
      'siyaset',
      'spor',
      'teknoloji',
      'turkiye',
      'yasam',
    ].each do |dir|
      # File.open(Rails.root.join(dir))
      files = FileList[Rails.root.join('news', dir)]

      files.each do |file|

      end
    end

  end
end
