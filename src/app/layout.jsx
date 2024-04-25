import { Inter, Lexend } from 'next/font/google'
import clsx from 'clsx'
import { GoogleAnalytics } from '@next/third-parties/google'

import '@/styles/tailwind.css'

export const metadata = {
  title: {
    template: '%s - AppleTune',
    default: 'AppleTune - Ringtone made easy',
  },
  description:
    'AppleTune is a platform that allows you to create and download ringtones for your iPhone, Android, and other devices.',
}

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

const lexend = Lexend({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-lexend',
})

export default function RootLayout({ children }) {
  return (
    <html
      lang="en"
      className={clsx(
        'h-full scroll-smooth bg-white antialiased',
        inter.variable,
        lexend.variable,
      )}
    >
      <body className="flex h-full flex-col">{children}</body>
      <GoogleAnalytics gaId="G-3V7EQDE0BD" />
    </html>
  )
}
