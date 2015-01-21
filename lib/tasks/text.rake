# encoding: utf-8

namespace :text do
  desc 'Veritabanı sıfırla'
  task :db_build => ['db:drop', 'db:create', 'db:migrate', 'db:seed']

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
      files = FileList[Rails.root.join('tmp', 'news', dir, '*')]

      files.each_with_index do |file, index|
        f = File.read(file)
        if n_index = f.index("\n")
          title = f[0..n_index-1].gsub("\n", " ").gsub("\r", " ").squish
          title = UnicodeUtils.downcase(title)
          content = f[n_index..-1].gsub("\n", " ").gsub("\r", " ").squish
          content = UnicodeUtils.downcase(content)
        else
          title = nil
          content = f.gsub("\n", " ").gsub("\r", " ").squish
          content = UnicodeUtils.downcase(content)
        end

        d = Datum.create(
          title: title,
          content: content,
          class_name: dir,
          file_name: File.basename(file),
          index_order: index + 1
        )

        puts d.errors.to_hash unless d.errors.empty?
      end
    end
  end

  desc 'veri bilgileri'
  task :info => :environment do
    Datum.group(:class_name).count.each do |class_name, value|
      puts "sınıf: #{class_name} \t-> #{value}"
    end
  end
end
